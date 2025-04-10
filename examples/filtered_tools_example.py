from examples.shared.apps import items
from examples.shared.setup import setup_logging

from fastapi_mcp import FastApiMCP

setup_logging()

# Example demonstrating how to filter MCP tools by operation IDs and tags

# Filter by including specific operation IDs
include_operations_mcp = FastApiMCP(
    items.app,
    name="Item API MCP - Included Operations",
    description="MCP server showing only specific operations",
    base_url="http://localhost:8000",
    include_operations=["get_item", "list_items"],
)

# Filter by excluding specific operation IDs
exclude_operations_mcp = FastApiMCP(
    items.app,
    name="Item API MCP - Excluded Operations",
    description="MCP server showing all operations except the excluded ones",
    base_url="http://localhost:8000",
    exclude_operations=["create_item", "update_item", "delete_item"],
)

# Filter by including specific tags
include_tags_mcp = FastApiMCP(
    items.app,
    name="Item API MCP - Included Tags",
    description="MCP server showing operations with specific tags",
    base_url="http://localhost:8000",
    include_tags=["items"],
)

# Filter by excluding specific tags
exclude_tags_mcp = FastApiMCP(
    items.app,
    name="Item API MCP - Excluded Tags",
    description="MCP server showing operations except those with specific tags",
    base_url="http://localhost:8000",
    exclude_tags=["search"],
)

# Combine operation IDs and tags (include mode)
combined_include_mcp = FastApiMCP(
    items.app,
    name="Item API MCP - Combined Include",
    description="MCP server showing operations by combining include filters",
    base_url="http://localhost:8000",
    include_operations=["delete_item"],
    include_tags=["search"],
)

# Mount all MCP servers with different paths
include_operations_mcp.mount(mount_path="/include-operations-mcp")
exclude_operations_mcp.mount(mount_path="/exclude-operations-mcp")
include_tags_mcp.mount(mount_path="/include-tags-mcp")
exclude_tags_mcp.mount(mount_path="/exclude-tags-mcp")
combined_include_mcp.mount(mount_path="/combined-include-mcp")

if __name__ == "__main__":
    import uvicorn

    print("Server is running with multiple MCP endpoints:")
    print(" - /include-operations-mcp: Only get_item and list_items operations")
    print(" - /exclude-operations-mcp: All operations except create_item, update_item, and delete_item")
    print(" - /include-tags-mcp: Only operations with the 'items' tag")
    print(" - /exclude-tags-mcp: All operations except those with the 'search' tag")
    print(" - /combined-include-mcp: Operations with 'search' tag or delete_item operation")
    uvicorn.run(items.app, host="0.0.0.0", port=8000)
